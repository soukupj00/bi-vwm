import React, {useState} from 'react';

import {FiSearch} from 'react-icons/fi';
import axios from "axios";

const Searchbar = (props) => {
    const [searchTerm, setSearchTerm] = useState('');

    // handle search form submission
    const handleSubmit = (event) => {
        event.preventDefault();
        const startTime = performance.now()
        axios.get('http://127.0.0.1:8000/songs', {
            params: {
                q: searchTerm
            }
        })
            .then((response) => {
                const endTime = performance.now()
                console.log(response.data);
                props.updateSongs(response.data);
                const responseTime = endTime - startTime
                console.log(`Response time: ${responseTime} ms`)
            })
            .catch((error) => {
                console.log(error);
            });
        setSearchTerm('')
    };

    return (
        <div className="flex justify-center mb-3">
            <form onSubmit={handleSubmit} autoComplete="off"
                  className="w-1/2 p-2 text-gray-400 focus-within:text-gray-600">
                <label htmlFor="search-field" className="sr-only">
                    Search all files
                </label>
                <div className="flex flex-row justify-start items-center">
                    <FiSearch aria-hidden="true" className="w-5 h-5 ml-4"/>
                    <input
                        name="search-field"
                        autoComplete="off"
                        id="search-field"
                        className="flex-1 bg-transparent border-none placeholder-gray-500 outline-none text-base text-white p-4"
                        placeholder="Search for songs using boolean query..."
                        type="search"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />
                    <button type="submit" className="text-white">Search</button>
                </div>
            </form>
        </div>
    );
};

export default Searchbar;
