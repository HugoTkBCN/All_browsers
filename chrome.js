function execution(command) {
    var exec = require('child_process').exec, child;

    child = exec(command,
    function (error, stdout, stderr) {
        console.log('stdout: ' + stdout);
        console.log('stderr: ' + stderr);
        if (error !== null) {
             console.log('exec error: ' + error);
        }
    });
    child();
}

function run_chrome() {
    var x = document.getElementById("form_chrome");
    var version = x.elements[0].value;
    execution("xhost +'local:docker@' && cd docker && python generate_docker_compose.py 71.0.3578.30");
}