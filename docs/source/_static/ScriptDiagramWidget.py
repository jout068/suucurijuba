import sys
from browser import window, ajax, document, timer, run_script as python_runner
from ScriptWidget import ScriptWidget, ScriptStderr

widget_code = """
<div class="app-container" id="app-container-{ID}">

  <div class="diagram-container" id="diagram-container-{ID}">
    <div id="diagram-{ID}" class="diagram-panel">
        <svg  id="svg-{ID}" xmlns="http://www.w3.org/2000/svg" width="345"></svg>
    </div>
  </div> 

  <div class="editor-container" id="app-container-{ID}">

    {SCRIPT_WIDGET}

    <div id="menu-{ID}" class="diagram-menu">
      <div class="buttons-row">
        <button class="diagram-button" id="restart-{ID}" type="button">Restart</button>
        <button class="diagram-button" id="next-{ID}" type="button">Next step</button>
      </div>
      <div id="variables-{ID}" class="diagram-variables">
            <div style="text-align: center">Wartości zmiennych:</div>
            <table style="width:100%%" id="variable-values-{ID}" >
            </table>

            <div style="text-align: center">Wartości wyrażeń:</div>
            <table style="width:100%%" id="expression-values-{ID}" >
            </table>
      </div>
    </div>

  </div>

 
</div>    
"""

class ScriptDiagramWidget:

  def __init__(self, script_name, main_div_id, diagram_maker_callback, **params):
    self.__script_widget = ScriptWidget(script_name,main_div_id,**dict(**params, read_only=True, hide_buttons=True))
    script_widget_code = document[main_div_id].innerHTML

    local_widget_code = widget_code.replace("{ID}",main_div_id)
    local_widget_code = local_widget_code.replace("{SCRIPT_WIDGET}", script_widget_code)
    m = main_div_id
    document[main_div_id].innerHTML = local_widget_code

    self.__diagram = diagram_maker_callback(document["svg-%s" % (m)], m)
    document["svg-%s" % (m)].attrs["height"] = self.__diagram.max_y()
    self.__diagram.start()
    self.__diagram.next_command.node.highlight()
    document["restart-%s" % (m)].bind("click",self.restart)
    document["next-%s" % (m)].bind("click",self.execute_next)

    # --- set up a table to monitor variables
    var_table = """<tr><th class="variable-name">zmienna</th><th class="variable-value">wartość</th></tr>"""
    for var_name in self.__diagram.list_variables():
        var_table += \
          """<tr><td id="label-%s-%s" class="label"> %s </td><td id="value-%s-%s"> %s </td></tr>""" \
          % (m,var_name,var_name,m,var_name,str(self.__diagram.get_value(var_name)))
    document["variable-values-%s" % m].innerHTML = var_table

    self.__expressions = []
    if "expressions" in params:
        e_i = 0
        expr_table = """<tr><th class="variable-name">zmienna</th><th class="variable-value">wartość</th></tr>"""
        for expr_name in params["expressions"]:
            self.__expressions.append(expr_name)
            try:
                value = eval(expr_name,self.__diagram.globals_copy())
            except:
                value = ""
            expr_table += \
              """<tr><td id="label-%s-e%d" class="label"> %s </td><td id="value-%s-e%d"> %s </td></tr>""" \
                % (m,e_i,expr_name,m,e_i,str(value))
            e_i += 1
        document["expression-values-%s" % m].innerHTML = expr_table

    self.__script_started = False

  def execute_next(self, event):
    if not self.__script_started: return

    #Range = window.ace.require('ace/range').Range
    if self.__diagram.next_command: self.__diagram.next_command.node.clear()
    if self.__diagram.has_next():
        m = self.__script_widget.main_div_id
        self.__diagram.next(False) # do not print debug messages
        if self.__diagram.next_command: 
            self.__diagram.next_command.node.highlight() # highlight the next box
            if len(self.__diagram.next_command.lines) > 0 :
              lines_from = self.__diagram.next_command.lines[0]
              lines_to = self.__diagram.next_command.lines[-1]
              #range = Range(lines_from, 0, lines_to+1, 0)
              #self.__script_widget.editor.session.addMarker(range, "ace_active-line", "text", True)
        
        # --- update variable values
        for var_name in self.__diagram.list_variables():
            if var_name.startswith("__"): continue
            document["value-%s-%s" % (m,var_name)].innerHTML = str(self.__diagram.get_value(var_name))

        # --- update expression values
        e_i = 0
        for expr_name in self.__expressions:
            try:
                value = eval(expr_name,self.__diagram.globals_copy())
            except:
                value = ""
            document["value-%s-e%d" % (m,e_i)].innerHTML = str(value)
            e_i += 1
    else:
        self.__script_started = False

  def restart(self, event):
    sys.stdout = self
    sys.stderr = ScriptStderr(self.__script_widget.console_pre_id)
    for var_name in self.__diagram.list_variables():
        if var_name.startswith("__"): continue
        self.__diagram.set_value(var_name,"")
        document["value-%s-%s" % (self.__script_widget.main_div_id,var_name)].innerHTML = \
                str(self.__diagram.get_value(var_name))
    self.__diagram.clear_all()
    self.__diagram.start()
    self.__diagram.next_command.node.highlight()
    self.__script_started = True

  def write(self, str): self.__script_widget.write(str)

