import React from "react";
import TweetItem from "./TweetItem";
import AddTweet from "./AddTweet";

class MainPage extends React.Component {
    

    render() {
        let tweets = [
            {
                title: "Hello, world!",
                content: "<h3>Just gonna type html here!</h3>",
            },
            { title: "Tweet", content: "<code>Code!</code>" },
            {
                title: "Nice!",
                content:
                    "<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Here's a link! I need to use single quotes for the href.</a>",
            },
            {
                title: "Hello, world!",
                content:
                    "<div>Typing <strong>using</strong> <em>more</em> <u>than</u> <sup>one</sup> <sub>html</sub> <del>tag</del>!</div>",
            },
        ];
        return (
            

       

            <React.Fragment>
                <div
                    className="w3-container w3-jumbo"
                    style={{ margin: "3rem", paddingLeft: "1rem" }}>
                    <h1> Tweets </h1>
                    <button className="w3-button w3-blue w3-large" onClick={() => {
                        document.getElementById("addTweet").style.display = "block"
                    }}>Add tweet</button>
                </div>
                <AddTweet />
                <div className="w3-container">
                    {tweets.map((item, index) => {
                        return (
                            <TweetItem
                                title={item.title}
                                content={item.content}
                                key={index}
                            />
                        );
                    })}
                </div>
            </React.Fragment>

            
        );
    }
}

export default MainPage;