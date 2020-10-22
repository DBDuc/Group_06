import React, { useState } from "react";
import { Button, FormGroup, FormControl } from "react-bootstrap";
import "./Login.css";

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

function validateForm() {
    return username.length > 0 && password.length > 0;
}

function handleSubmit(event) {
    event.preventDefault();
}

return (
    <div className="Login">
        <form onSubmit={handleSubmit}>
            <FormGroup controlId="username" bsSize="large">
                <label>Username</label>          
                <FormControl
                    type="text"
                    value={username}
                    onChange={e => setUsername(e.target.value)}
                />
            </FormGroup>        
            <FormGroup controlId="password" bsSize="large">
                <label>Password</label>          
                <FormControl            
                    type="password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                />
            </FormGroup>        
            <Button block bsSize="large" disabled={!validateForm()} type="submit">
                Login
            </Button>      
        </form>
    </div>
);
}