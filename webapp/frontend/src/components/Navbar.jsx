import React from "react";

function Navbar() {
    return (
        <div className="w3-bar w3-black">
            <a className="w3-bar-item w3-button" href="/">
                TwitterClone
            </a>
            <div style={{ float: "right" }}>
                <a className="w3-bar-item w3-button" href="/login">
                    Log In
                </a>
                <a className="w3-bar-item w3-button" href="/register">
                    Sign Up
                </a>
            </div>
        </div>
    );
}

export default Navbar;