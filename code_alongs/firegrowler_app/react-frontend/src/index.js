import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import {Redirect} from 'react-router';
import Login from './Login';
import App from './App';

ReactDOM.render(
  <Router>
    <div>
      <Route exact path="/" component={Login}/>
      <Route path="/app" component={App} />
      <Route path="*" render={()=>{
        return <Redirect to="/" />
      }} />
    </div>
  </Router>,
  document.getElementById('root')
);
