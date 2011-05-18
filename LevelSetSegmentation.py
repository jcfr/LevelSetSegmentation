from __main__ import vtk, qt, ctk, slicer
#
# Level Set Segmentation using VMTK based Tools
#

class LevelSetSegmentation:
  def __init__(self, parent):
    parent.title = "LevelSetSegmentation"
    parent.category = ""
    parent.contributor = "--"
    parent.helpText = """dsfdsf"""
    parent.acknowledgementText = """sdfsdfdsf"""
    self.parent = parent

class LevelSetSegmentationWidget:
  def __init__(self, parent=None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()

    if not parent:
      self.setup()
      self.parent.show()
    
  def setup(self):
    
      workflow = ctk.ctkWorkflow()
      
    
      workflowWidget = ctk.ctkWorkflowStackedWidget()
      workflowWidget.setWorkflow(workflow)
    
      steps = []
    
      steps.append(ExampleStep('step1'))
      steps.append(ExampleStep('step2'))
      steps.append(ExampleStep('step3'))
    
      # Add transition associated to steps
      for i in range(len(steps) - 1):
        workflow.addTransition(steps[i], steps[i + 1])
    
      workflow.start()
    
      workflowWidget.visible = True
      self.layout.addWidget(workflowWidget)    


class ExampleStep(ctk.ctkWorkflowWidgetStep) :
  """Step implemented using the derivation approach"""
  
  def __init__(self, stepid):
    self.initialize(stepid)
    
  def createUserInterface(self):
    layout = qt.QVBoxLayout(self)
    label = qt.QLabel("This is %s" % self.id())
    layout.addWidget(label)
  
  def onEntry(self, comingFrom, transitionType):
    comingFromId = "None"
    if comingFrom: comingFromId = comingFrom.id()
    print "-> onEntry - current [%s] - comingFrom [%s]" % (self.id(), comingFromId)
    super(ExampleStep, self).onEntry(comingFrom, transitionType)
    
  def onExit(self, goingTo, transitionType):
    goingToId = "None"
    if goingTo: goingToId = goingTo.id()
    print "-> onExit - current [%s] - goingTo [%s]" % (self.id(), goingToId)
    super(ExampleStep, self).onExit(goingTo, transitionType)
    
  def validate(self, desiredBranchId):
    validationSuceeded = True
    print "-> validate %s" % self.id()
    
    super(ExampleStep, self).validate(validationSuceeded, desiredBranchId)


