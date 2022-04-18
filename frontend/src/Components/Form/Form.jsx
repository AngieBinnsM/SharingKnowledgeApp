import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { addKnowledge, noValue } from "../../Data/KnowledgeSlice";
import { putIdea } from "../../Data/KnowledgeSlice";

function Form() {
  const dispatch = useDispatch();
  const [user, setUser] = useState("");
  const [title, setTitle] = useState("");
  const [technology, setTechnology] = useState("");
  const [link, setLink] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (user && title && technology && link && description) {
      dispatch(
        putIdea({
          load: {
            id: new Date().getTime().toString(),
            user,
            technology,
            title,
            link,
            description,
          },
        })
      );

      setUser("");
      setTechnology("");
      setTitle("");
      setLink("");
      setDescription("");
    } else {
      dispatch(noValue());
    }
  };
  return (
    <form onSubmit={handleSubmit}>
      <div className="row">
        <div className="form-group col-md-6">
          <label htmlFor="user"> User: </label>
          <input
            className="form-control"
            type="text"
            id="user"
            name="user"
            value={user}
            onChange={(e) => setUser(e.target.value)}
          />
        </div>

        <div className="form-group col-md-6">
          <label htmlFor="technology"> Technology: </label>
          <input
            className="form-control"
            type="text"
            id="technology"
            name="technology"
            value={technology}
            onChange={(e) => setTechnology(e.target.value)}
          />
        </div>
      </div>

      <div className="row">
        <div className="form-group col-md-6">
          <label htmlFor="title"> Title: </label>
          <input
            className="form-control"
            type="text"
            id="title"
            name="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>

        <div className="form-group col-md-6">
          <label htmlFor="link"> Url: </label>
          <input
            className="form-control"
            type="text"
            id="link"
            name="link"
            value={link}
            onChange={(e) => setLink(e.target.value)}
          />
        </div>
      </div>

      <div className="form-group" style={{ marginBottom: "10px" }}>
        <label htmlFor="description"> Description: </label>
        <input
          className="form-control"
          type="text"
          id="description"
          name="descripction"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <button type="submit" className="btn btn-primary">
        {" "}
        Submit{" "}
      </button>
    </form>
  );
}

export default Form;
