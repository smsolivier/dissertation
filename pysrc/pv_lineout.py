#!/usr/bin/python3
# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

import sys 
inp = sys.argv[1]
out = sys.argv[2]

# create a new 'PVD Reader'
ip1pvd = PVDReader(registrationName='pv.pvd', FileName=inp)
ip1pvd.CellArrays = ['attribute']
ip1pvd.PointArrays = ['phi']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
ip1pvdDisplay = Show(ip1pvd, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
ip1pvdDisplay.Representation = 'Surface'
ip1pvdDisplay.ColorArrayName = [None, '']
ip1pvdDisplay.SelectTCoordArray = 'None'
ip1pvdDisplay.SelectNormalArray = 'None'
ip1pvdDisplay.SelectTangentArray = 'None'
ip1pvdDisplay.OSPRayScaleArray = 'phi'
ip1pvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ip1pvdDisplay.SelectOrientationVectors = 'None'
ip1pvdDisplay.ScaleFactor = 0.1
ip1pvdDisplay.SelectScaleArray = 'None'
ip1pvdDisplay.GlyphType = 'Arrow'
ip1pvdDisplay.GlyphTableIndexArray = 'None'
ip1pvdDisplay.GaussianRadius = 0.005
ip1pvdDisplay.SetScaleArray = ['POINTS', 'phi']
ip1pvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
ip1pvdDisplay.OpacityArray = ['POINTS', 'phi']
ip1pvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
ip1pvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
ip1pvdDisplay.PolarAxes = 'PolarAxesRepresentation'
ip1pvdDisplay.ScalarOpacityUnitDistance = 0.1767766952966369
ip1pvdDisplay.OpacityArrayName = ['POINTS', 'phi']
ip1pvdDisplay.ExtractedBlockIndex = 2

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ip1pvdDisplay.ScaleTransferFunction.Points = [0.15750140203584487, 0.0, 0.5, 0.0, 2.9343383267110847, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ip1pvdDisplay.OpacityTransferFunction.Points = [0.15750140203584487, 0.0, 0.5, 0.0, 2.9343383267110847, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5, 0.5, 10000.0]
renderView1.CameraFocalPoint = [0.5, 0.5, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(ip1pvdDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
ip1pvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# Properties modified on ip1pvd
ip1pvd.CellArrays = []

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(ip1pvdDisplay, ('POINTS', 'phi'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
ip1pvdDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
ip1pvdDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'phi'
phiLUT = GetColorTransferFunction('phi')

# get opacity transfer function/opacity map for 'phi'
phiPWF = GetOpacityTransferFunction('phi')

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=ip1pvd,
    Source='Line')

# init the 'Line' selected for 'Source'
# triple point line position
# plotOverLine1.Source.Point1 = [3.5, 0, 0.0]
# plotOverLine1.Source.Point2 = [3.5, 3, 0.0]
# square line position 
plotOverLine1.Source.Point1 = [0, .5, 0.0]
plotOverLine1.Source.Point2 = [1.0, .5, 0.0]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'phi']
plotOverLine1Display.LookupTable = phiLUT
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'arc_length'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'None'
plotOverLine1Display.ScaleFactor = 0.1
plotOverLine1Display.SelectScaleArray = 'None'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'None'
plotOverLine1Display.GaussianRadius = 0.005
plotOverLine1Display.SetScaleArray = ['POINTS', 'arc_length']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'arc_length']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['phi']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'phi', 'phi', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'phi', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Z', '1', '0.5000076295109483', '0', 'Points_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'phi', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'phi', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'phi', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'phi', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'phi', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'phi', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'phi', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'phi', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'phi', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'phi', '4', 'vtkValidPointMask', '4']

# update the view to ensure updated data information
lineChartView1.Update()

# save data
SaveData(out, proxy=plotOverLine1, PointDataArrays=['arc_length', 'phi', 'vtkValidPointMask'])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(3108, 1136)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5, 0.5, 10000.0]
renderView1.CameraFocalPoint = [0.5, 0.5, 0.0]
renderView1.CameraParallelScale = 0.7071067811865476

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).