import frida, sys

def on_message(message, data):
    print(message)

PACKAGE_NAME = "uncrackable1"

jscode = """
console.log("[+] Start Script");

Java.perform(function(){
    console.log("[+] Hooking exit()");
    var systemClass = Java.use("java.lang.System");
    systemClass.exit.implementation = function(){
        console.log("[+] exit() called");
    }
});

Java.perform(function(){
    console.log("[+] Hooking sg.vantagepoint.a.a.a()");
    var aClass = Java.use("sg.vantagepoint.a.a");
    aClass.a.implementation = function(arg1, arg2){
        var str = this.a(arg1, arg2);
        var flag = "";

        for(var i = 0; i < str.length; i++){
            flag += String.fromCharCode(str[i]);
        }
        console.log("[+] flag : " + flag);
        return str;
    }
});
"""

process = frida.get_usb_device(1).attach(PACKAGE_NAME)
script = process.create_script(jscode)
script.on("message", on_message)
print("[*] Running Hook")
script.load()
sys.stdin.read()