def add_eye_ball(self, pose, orientation):
        # Eye ball
        sphere = vtk.vtkSphereSource()
        sphere.SetThetaResolution(64)
        sphere.SetPhiResolution(64)
        sphere.SetRadius(0.5)

        reader = vtk.vtkJPEGReader()
        reader.SetFileName(os.path.join(rospkg.RosPack().get_path('motion_renderer'), 'resource', 'green_eye.jpg'))

        texture = vtk.vtkTexture()
        texture.SetInputConnection(reader.GetOutputPort())

        map_to_sphere = vtk.vtkTextureMapToSphere()
        map_to_sphere.SetInputConnection(sphere.GetOutputPort())
        map_to_sphere.PreventSeamOn()

        xform = vtk.vtkTransformTextureCoords()
        xform.SetInputConnection(map_to_sphere.GetOutputPort())
        xform.SetScale(1.5, 1.5, 1)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(xform.GetOutputPort())

        # Left Eye Actor
        eye_actor = vtk.vtkActor()
        eye_actor.SetMapper(mapper)
        eye_actor.SetTexture(texture)
        eye_actor.SetPosition(pose[0], pose[1], pose[2])
        eye_actor.RotateX(orientation[0])
        eye_actor.RotateY(orientation[1])
        eye_actor.RotateZ(orientation[2])

        self.ren.AddActor(eye_actor)
        return eye_actor 
