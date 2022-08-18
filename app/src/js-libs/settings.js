class LocalStorage{
    constructor () {}

    get keyboard_status(){
        return localStorage.getItem("keyboard-status")
    }
    set keyboard_status(status){
        //status: Boolean
        localStorage.setItem("keyboard-status", status)        
    }
}

export default LocalStorage