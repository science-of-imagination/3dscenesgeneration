filename = "path_to_\\964"
to_open = String.new(filename)
result = Sketchup.open_file to_open.concat(".skp")
model = Sketchup.active_model

status = model.export filename.concat(".dae")