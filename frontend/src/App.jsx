import './App.css'
import {BrowserRouter, Routes, Route} from "react-router-dom";
import {Game} from "./pages/Game.jsx";
import {Success} from "./pages/Success.jsx";

function App() {

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Game />} />
                <Route path="/success" element={<Success />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App
