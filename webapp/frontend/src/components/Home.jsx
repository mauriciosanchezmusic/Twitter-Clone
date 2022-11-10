import React from "react";

function Home() {
    return (
        <React.Fragment>
            <div
                className="w3-container w3-center w3-blue"
                style={{ padding: "2rem" }}>
                <h1 className="w3-jumbo" style={{border: "solid"}}>TwitterClone</h1>
                <br></br><br></br><br></br><br></br><br></br><br></br>
                <button
                    className="w3-button w3-pink"
                    style={{ marginRight: "1rem",fontSize:'50px' }}>
                    <a  href="/login">
                    Log In
                    </a>

                </button>
                <br></br><br></br><br></br><br></br><br></br>
                <button className="w3-button w3-pink"
                style={{ marginRight: "1rem",fontSize:'50px' }}>
                    <a  href="/register">
                    Register
                    </a>
                </button>
                <br></br><br></br><br></br><br></br>
            </div>
        </React.Fragment>
    );
}

export default Home;