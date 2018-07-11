scene_graph = {
    "objects": [],
    "relationships": []
}


class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    scene_graph.objects.push(this.state.value);
    console.log(scene_graph);
    // alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
    this.setState(this.state);
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Objects:
            <input type="text" value={this.state.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
        <ul>
            {  scene_graph.objects.map(function(object){ return <li>{object}</li> })}
        </ul>
      </div>
    );
  }
}



ReactDOM.render(
  <NameForm />,
  document.getElementById('text-box')
);
