/*
{
  text: action.payload,
  id: state.length+1,
  i: state.length
}
*/

export default function todoReducer(state=[], action){
  switch(action.type){
    case 'ADD_TODO':
      const newItem = {
        text: action.payload,
        id: state.length+1,
        i: state.length
      }
      return [newItem, ...state]
    break;
    case 'REMOVE_TODO':
      // console.log("REMOVE TODO: ", action.payload, state)
      // return [
      //   ...state.slice(0,action.payload.i),
      //   ...state.slice(action.payload.i+1)
      // ]
      return state.filter(todo => todo.i != action.payload)
    break;
    case 'EDIT_TODO':
    return state.map((todo) => {
      if(todo.i === action.payload.i){
        todo.text = action.payload.text
      }
    })
    break;
    default:
      return state
    break;
  }
}
