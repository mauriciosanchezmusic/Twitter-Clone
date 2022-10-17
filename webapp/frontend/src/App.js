import React from "react";
import Home from "./components/Home";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import Register from "./components/Register";
import { BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";


function App() {
    return (
        <React.Fragment>
            <Navbar />
            <Router>
                <Routes> 
                    <Route exact path='/' element={< Home />}></Route>
                    <Route exact path='/login' element={< Login />}></Route>
                    <Route exact path='/register' element={< Register />}></Route>
                </Routes>
            </Router>
        </React.Fragment>
    );
}

export default App;