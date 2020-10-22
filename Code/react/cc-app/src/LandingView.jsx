import React, {Component} from "react";
import axios from "axios";
axios.defaults.baseURL = "https://localhost/deals";

class LandingView extends Component {
    constructor() {
        super();
        this.state = {
            context: []
        };
    }

    render() {
        return (
            <div className= "viewer">
                <table className="table">
                    <thead>
                        <tr>
                            <th>Instrument</th>
                            <th className="num">Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {/* {this.state.context.map(x =>
                            <tr key={x.deals.Instrumentname}
                            )} */}
                    </tbody>



                </table>
            </div>
        );


    }

    get = () => {
        axios.get("/posts").then(result => {
            console.log(result.data);
            this.setState({ context: result.data});
        });
    };
        
    }

    export default LandingView;