import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { deletee } from "../../Data/KnowledgeSlice";
import { Button } from "react-bootstrap";
import { Card } from "react-bootstrap";
import { body } from "./style";
import ReactPlayer from "react-player";
import CardImg from "./CardImg3.jpg";

function SmallCard() {
  const know = useSelector((state) => state.knowledge.idea);
  const dispatch = useDispatch();

  function startWith(str) {
    return str.startsWith("https://www.youtube.com/");
  }

  return (
    <section style={body}>
      {know.map((point) => (
        <Card
          style={{
            width: "20rem",
            boxShadow: "0 0 12px rgba(0,0,0,0.5)",
            borderRadius: "15px",
          }}
        >
          <Card.Body>
            {startWith(point.link) ? (
              <ReactPlayer
                url={point.link}
                width="282px"
                height="159px"
                muted="false"
                playing="true"
              ></ReactPlayer>
            ) : (
              <img
                src={CardImg}
                style={{ width: "318px", height: "159px", marginLeft: "-16px" }}
                alt="..."
              ></img>
            )}

            <Card.Header>
              <Card.Title>{point.technology}</Card.Title>
            </Card.Header>

            <Card.Subtitle
              className="mb-2 text-muted"
              style={{ marginTop: "10px" }}
            >
              {point.title}
            </Card.Subtitle>
            <Card.Text>{point.description}</Card.Text>
            <footer className="blockquote-footer">{point.user}</footer>
            <a href={point.link} className="btn btn-secondary me-2" target="_">
              Link
            </a>
            <Button
              variant="primary"
              onClick={() => dispatch(deletee({ id: point.id }))}
            >
              Delete
            </Button>
          </Card.Body>
        </Card>
      ))}
    </section>
  );
}

export default SmallCard;
