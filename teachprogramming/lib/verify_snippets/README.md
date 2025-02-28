


* Verify Full file - verify/compile the syntax (not not run it!)
    * python
        * just run ast parser? py_compile? mypy
        * `python3 -m py_compile tictactoe_udp.py`
    * java
        * correct filename for top level class
        * javac
    * csharp
        * correct file? and manifest - fucks sake
    * html5/js
        * how could this be possible?
    * c?
    * lua?

* pytest?
* find all project `.json` files and iterate
* Input versions `.json` and get full file iterator (language, f'language_version.ext')
* Register task with task runner
* Prepare tempfolder
    * correct filename (seek code? fallback to given name)
    * create manifest
* run language container + mount tempfolder at workdir + cmd compile (not the same as container default)
    * exit code non zero == fail
* output pass/fail