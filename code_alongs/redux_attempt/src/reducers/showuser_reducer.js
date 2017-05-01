export default function(state={}, action){
  switch(action.type){
    case 'SELECT_USER':
      const newState = state;
      console.log('state is: ', newState)
      return action.payload
    break;
    case 'ADD_USER':
      console.log('action is: ', action);
      console.log('state.users is: ', state.users);
      console.log('state.showusers is: ', state.showusers);
      return action.payload
    break;
    default:
      return state;

  }
}
