import './app.css'
import App from './App.svelte'
import "flex-splitter-directive/styles.min.css";
import "flex-splitter-directive";
import 'bootstrap/dist/css/bootstrap.min.css';

const app = new App({
  target: document.getElementById('app')
})

export default app
