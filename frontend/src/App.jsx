import {Route, Routes} from 'react-router-dom';

import {Searchbar} from './components';
import {HomePage, SongDetail} from './pages';
import Navbar from "./components/Navbar";
import React, {useState} from "react";

const App = () => {
    const [songList, setSongs] = useState(null);

    return (
        <div className="relative flex">
            <div className="flex-1 flex flex-col bg-gradient-to-br from-black to-[#121286]">
                <Navbar/>
                <Searchbar updateSongs={setSongs}/>
                <div
                    className="px-6 h-[calc(100vh-72px)] overflow-y-scroll hide-scrollbar flex xl:flex-row flex-col-reverse">
                    <div className="flex-1 h-fit pb-40">
                        <Routes>
                            <Route path="/" element={<HomePage songs={songList}/>}/>
                            <Route path="/songs/:id" element={<SongDetail/>}/>
                        </Routes>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default App;
