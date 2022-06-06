import http.server, pathlib, functools
http.server.test(
	functools.partial(
		http.server.SimpleHTTPRequestHandler, 
		directory=str(
			pathlib.Path().home().joinpath(
				"OneDrive - Canterbury Christ Church University", 
				"Desktop",
			)
		)
	)
)
# Serve CCCU desktop via http on port 8000
# http://localhost:8000
# Copy and paste the text above into a python3 terminal