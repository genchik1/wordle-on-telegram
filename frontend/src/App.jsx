import './App.css'
import {BrowserRouter, Routes, Route} from "react-router-dom";
import {Game} from "./pages/Game.jsx";

function App() {

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Game />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App
