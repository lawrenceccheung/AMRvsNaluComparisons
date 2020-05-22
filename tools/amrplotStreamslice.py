# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import sys

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'AMReX/BoxLib Grid Reader'
pltfile=sys.argv[1]
plt40000 = AMReXBoxLibGridReader(FileNames=[pltfile])
plt40000.CellArrayStatus = []

# Properties modified on plt40000
plt40000.CellArrayStatus = ['temperature', 'velocityx', 'velocityy', 'velocityz']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1071, 759]

# get layout
layout1 = GetLayout()

# show data in view
plt40000Display = Show(plt40000, renderView1, 'AMRRepresentation')

# trace defaults for the display properties.
plt40000Display.Representation = 'Outline'
plt40000Display.ColorArrayName = [None, '']
plt40000Display.OSPRayScaleFunction = 'PiecewiseFunction'
plt40000Display.SelectOrientationVectors = 'None'
plt40000Display.ScaleFactor = 192.0
plt40000Display.SelectScaleArray = 'None'
plt40000Display.GlyphType = 'Arrow'
plt40000Display.GlyphTableIndexArray = 'None'
plt40000Display.GaussianRadius = 9.6
plt40000Display.SetScaleArray = [None, '']
plt40000Display.ScaleTransferFunction = 'PiecewiseFunction'
plt40000Display.OpacityArray = [None, '']
plt40000Display.OpacityTransferFunction = 'PiecewiseFunction'
plt40000Display.DataAxesGrid = 'GridAxesRepresentation'
plt40000Display.PolarAxes = 'PolarAxesRepresentation'
plt40000Display.ScalarOpacityUnitDistance = 21.025936326226777

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(Input=plt40000)
calculator1.AttributeType = 'Cell Data'
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'UMag'
calculator1.Function = 'sqrt(velocityx^2 + velocityy^2 + velocityz^2)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'AMRRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Outline'
calculator1Display.ColorArrayName = ['CELLS', '']
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 192.0
calculator1Display.SelectScaleArray = 'UMag'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'UMag'
calculator1Display.GaussianRadius = 9.6
calculator1Display.SetScaleArray = [None, '']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = [None, '']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 21.025936326226777

# hide data in view
Hide(plt40000, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(Input=calculator1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [768.0, 768.0, 960.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [768.0, 768.0, 960.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [1.0, -1.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'UMag'
uMagLUT = GetColorTransferFunction('UMag')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['CELLS', 'UMag']
slice1Display.LookupTable = uMagLUT
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 192.0
slice1Display.SelectScaleArray = 'UMag'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'UMag'
slice1Display.GaussianRadius = 9.6
slice1Display.SetScaleArray = [None, '']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = [None, '']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'UMag'
uMagPWF = GetOpacityTransferFunction('UMag')

# reset view to fit data
renderView1.ResetCamera()

# hide data in view
Hide(calculator1, renderView1)

# set active source
SetActiveSource(plt40000)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# set active source
SetActiveSource(slice1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice1.SliceType)

# Rescale transfer function
uMagLUT.RescaleTransferFunction(4.5, 7.5)

# Rescale transfer function
uMagPWF.RescaleTransferFunction(4.5, 7.5)

# set active source
SetActiveSource(calculator1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# current camera placement for renderView1
renderView1.CameraPosition = [5523.734848235029, -3987.7348787526043, 960.0000000000001]
renderView1.CameraFocalPoint = [767.9999847412109, 767.9999847412109, 960.0000000000001]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1740.7197737020563

# get color legend/bar for uMagLUT in view renderView1
fontsize=4
uMagLUTColorBar = GetScalarBar(uMagLUT, renderView1)
uMagLUTColorBar.ScalarBarLength = 0.250
uMagLUTColorBar.ScalarBarThickness = 2
uMagLUTColorBar.TitleFontSize = fontsize #10 
uMagLUTColorBar.LabelFontSize = fontsize #10  
uMagLUTColorBar.Position = [0.9, 0.25]

# save screenshot
outfile1=sys.argv[2]
SaveScreenshot(outfile1, renderView1, ImageResolution=[1200, 850],
    OverrideColorPalette='WhiteBackground', 
    # PNG options
    CompressionLevel='3')

# set active source
SetActiveSource(slice1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice1.SliceType)

# set scalar coloring
ColorBy(slice1Display, ('CELLS', 'temperature'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uMagLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'temperature'
temperatureLUT = GetColorTransferFunction('temperature')
temperatureLUT.RescaleTransferFunction(290.0, 300.0)

# get opacity transfer function/opacity map for 'temperature'
temperaturePWF = GetOpacityTransferFunction('temperature')
temperaturePWF.RescaleTransferFunction(290.0, 300.0)

# set active source
SetActiveSource(calculator1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# current camera placement for renderView1
renderView1.CameraPosition = [5523.734848235029, -3987.7348787526043, 960.0000000000001]
renderView1.CameraFocalPoint = [767.9999847412109, 767.9999847412109, 960.0000000000001]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1740.7197737020563

# get color legend/bar for uMagLUT in view renderView1
fontsize=4
TColorBar = GetScalarBar(temperatureLUT, renderView1)
TColorBar.ScalarBarLength = 0.250
TColorBar.ScalarBarThickness = 2
TColorBar.TitleFontSize = fontsize #10 
TColorBar.LabelFontSize = fontsize #10  
TColorBar.Position = [0.9, 0.25]

# save screenshot
outfile2=sys.argv[3]
SaveScreenshot(outfile2, renderView1, ImageResolution=[1200, 850],
    OverrideColorPalette='WhiteBackground',
    # PNG options
    CompressionLevel='3')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [5523.734848235029, -3987.7348787526043, 960.0000000000001]
renderView1.CameraFocalPoint = [767.9999847412109, 767.9999847412109, 960.0000000000001]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 1740.7197737020563

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
