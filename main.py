import vtkmodules.all as vtk

# Load the STL file
reader = vtk.vtkSTLReader()
reader.SetFileName("mball.stl")  # Replace with your file path

# Create a mapper and actor
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# ... (previous code)

# Create a renderer and render window
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create a render window interactor
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# Add the actor to the renderer
renderer.AddActor(actor)

# Set up camera and render
renderer.ResetCamera()
render_window.Render()
render_window_interactor.Start()
