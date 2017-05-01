export default function(i) {
  console.log('index remove:', i)
  return {
    type: 'REMOVE_TODO',
    payload: i
  }
}
