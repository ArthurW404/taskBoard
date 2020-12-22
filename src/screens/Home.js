import React, { useEffect, useState } from "react";
import BoardCard from "../components/BoardCard";

const Home = () => {
  const [boards, setBoards] = useState([]);
  const getBoards = () => {
    return [];
  };
  useEffect(() => {
    const boards = getBoards();
    setBoards(boards);
  }, []);

  const boardsView = boards.map((board) => {
    return <BoardCard />;
  });

  return (
    <div class="container">
      <h1>My boards</h1>

      {boardsView}

      <br />
      <button
        type="button"
        class="btn btn-primary"
        data-toggle="modal"
        data-target="#add_board_modal"
      >
        Add new board
      </button>
    </div>
  );
};

export default Home;
