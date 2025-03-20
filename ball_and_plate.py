import genesis as gs

def init_scene_and_cam():
    gs.init(backend=gs.cpu)

    scene = gs.Scene(show_viewer=False)

    # Floor as the ground.
    floor = scene.add_entity(gs.morphs.Plane())

    # Ball, slightly above the plate.
    ball = scene.add_entity(
        gs.morphs.Sphere(pos=(0, 0, 1.01), radius=0.05)
    )

    # Plate as a Box.
    plate = scene.add_entity(
        gs.morphs.Box(pos=(0, 0, 1), size=(0.5, 0.5, 0.1))
    )

    # Create a static base for the plate support.
    base = scene.add_entity(
        gs.morphs.Box(pos=(0, 0, 1), size=(0.1, 0.1, 0.1))
    )

    # Add a joint to connect the plate to the base.
    # Here we use a revolute joint as an example, which allows rotation about one axis.
    joint = scene.add_joint(
        type=gs.joints.RevoluteJoint,
        entity_a=plate,
        entity_b=base,
        pivot=(0, 0, 1),   # The pivot location in world coordinates.
        axis=(0, 1, 0)     # The axis of rotation; adjust as needed.
    )

    # Add a camera.
    cam = scene.add_camera(
        res    = (1280, 960),
        pos    = (4, 0.0, 2),
        lookat = (0, 0, 0),
        fov    = 50,
    )

    return scene, cam

def simulate(scene, cam):
    for i in range(120):
        scene.step()
        cam.render()
    cam.stop_recording(save_to_filename='out/b&p.mp4', fps=60)

def main():
    scene, cam = init_scene_and_cam()
    scene.build()
    gs.tools.run_in_another_thread(fn=simulate, args=(scene, cam))
    cam.start_recording()

if __name__ == "__main__":
    main()
