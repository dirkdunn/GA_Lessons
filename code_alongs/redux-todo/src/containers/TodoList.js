import React, {Component} from 'react';
import {connect} from 'react-redux';
import removeTodo from '../actions/remove_todo';
import editTodo from '../actions/edit_todo';
import {bindActionCreators} from 'redux';


class TodoList extends Component {

  constructor(props){
    super(props)

    this.state = {
      edit: false,
      editInput: ''
    }
  }

  removeTodo(id){
    this.props.removeTodo(id);
  }


  startEdit(todo){
    this.setState({edit: !this.state.edit})
  }

  editTodo(){

  }

  render(){
    console.log('props: ', this.props)
    const todos = this.props.todos.map(todo => {
      return (
        <li key={todo.id} className="list-group-item" style={{overflow: 'auto'}}>
          <span>{todo.text}</span>

          <button className="btn btn-danger"
          style={{ float: 'right' }}
          onClick={ e => this.removeTodo(todo.i) }>
          Delete</button>

          <button className="btn btn-success"
          style={{float: 'right', marginRight: '.5em'}}
          onClick={e => this.startEdit(todo)}>
          Edit
          </button>

          <form className="form-inline" style={{display: this.state.edit ? 'block' : 'none'}}>
            <input type="text" className="form-control" />
            <button type="submit">Change</button>
          </form>
        </li>)
    })

    return(
      <div className="col-sm-6 col-sm-offset-3" style={{marginTop: '1em'}}>
        <ul className="list-group">
          {todos}
        </ul>
      </div>)
  }
}

function mapStateToProps(state){
  // console.log('state: ', state)
  return {
    todos: state.todos
  }
}

function mapDispatchToProps(dispatch){
  return bindActionCreators({
    removeTodo: removeTodo,
    editTodo: editTodo
  },dispatch);
}


export default connect(mapStateToProps,mapDispatchToProps)(TodoList)
