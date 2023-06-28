import React from 'react';
import {Link} from "react-router-dom";

const Navbar = () => (
    <nav className="flex items-center justify-between flex-wrap p-6">
        <div className="flex items-center text-white mr-6">
            <span className="font-bold text-xl">Lyric Finder App</span>
        </div>
        <div className="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
            <div className="text-l lg:flex-grow">
                <Link to="/" className="block mt-4 lg:inline-block lg:mt-0 text-blue-200 hover:text-white mr-4">
                    Home
                </Link>
            </div>
        </div>
    </nav>
);

export default Navbar;
