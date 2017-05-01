export default (e,first, last, description) => {
  e.preventDefault()
  console.log('user is: ',first,last,description);

  return {
    type: 'ADD_USER',
    payload: {
      first : first,
      last : last,
      description : description
    }
  }
}
