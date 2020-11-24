import React, { Component } from 'react';
import App from './App';
import './css/Intro.css';


class Intro extends React.Component {
    constructor() {
        super();
        this.state = { 
            msg: 'Hello, World',
            flag: 0
        }
    }

    changeMsg = () => {
        let flag = this.state.flag;
        if(flag == 0) {
            this.setState({ 
                msg: 'My name is Heeyeon.',
                flag: 1
            })
        }
        else if(flag == 1) {
            this.setState({
                msg: 'Welcome to my world.',
                flag: 2
            })
        }
        else if(flag == 2) {
            this.setState({
                flag: 3
            })
        }
        else {
            console.log("Error in changeMsg");
        }
    }
    render() {   
        let flag = this.state.flag;
        if (flag == 3) {
            return <App />
        }
        else {
            return ( 
                <body className="Intro_body" onClick={this.changeMsg}>
                    <div className="Intro_div">
                        <p className="Intro_p">
                            {this.state.msg}
                        </p>        
                    </div>
                </body>
            );
        }
    }
}

export default Intro;