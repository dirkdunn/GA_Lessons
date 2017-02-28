import React from 'react'
import { render } from 'react-dom'
import App from './modules/App'
import About from './modules/About'
import Repos from './modules/Repos'
import { Router, Route, hashHistory } from 'react-router'


render(
  <Router history={hashHistory}>
    {/* Nest the other routes inside of the parent route */}
    <Route path="/" component={App}>
      <Route path="/repos" component={Repos}/>
      <Route path="/about" component={About}/>
    </Route>
  </Router>
,document.getElementById('app'))
