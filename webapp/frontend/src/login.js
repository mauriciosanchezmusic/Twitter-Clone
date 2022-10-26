import Axios from "axios";

async function login(email, pwd) {
    const res =await Axios.post("http://localhost:3000/api/login", {email, pwd});
    const {data} = await res;
    if (data.error) {
        return data.error
    } else {
        localStorage.setItem("token", data.token);
        return true
    }
}

function check() {
    if (localStorage.getItem("token")) {
        return true;
    } else {
        return false;
    }
}

export {login, check};