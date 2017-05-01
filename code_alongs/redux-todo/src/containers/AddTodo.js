import React, {Component} from 'react';
import addTodo from '../actions/add_todo';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';


class AddTodo extends Component {
  constructor(props){
      super(props)
      this.state = {
        input: ''
      }
  }

  addTodo(e){
    e.preventDefault();
    this.props.addTodo(this.state.input);
    this.setState({input: ''})
  }

  render(){
    return(
      <div className="col-sm-6 col-sm-offset-3">
      <h1>Redux Todo:</h1>
        <form onSubmit={this.addTodo.bind(this)} className="add-todo form-inline">
          <input type="text" placeholder="add todo.." value={this.state.input} className="form-control"
          onChange={ e => this.setState({input:e.target.value}) }/>
          <button type="submit" className="btn btn-primary">Submit</button>
        </form>
      </div>
    )
  }
}

function mapDispatchToProps(dispatch){
  return bindActionCreators({
    addTodo
  },dispatch)
}

export default connect(null,mapDispatchToProps)(AddTodo)
