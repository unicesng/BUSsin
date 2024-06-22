import { Input, Button } from '@chakra-ui/react'
import { Link } from 'react-router-dom'

const SearchBar = () => {

    const handleClick = () => {

    }

    return (
        <div className='flex'>
            <Input placeholder='Search bus stop or bus...' className="m-4" />
            <Link to="/Results">
                <Button colorScheme='blue' onClick={handleClick}>Enter</Button>
            </Link>
        </div>
    )
}

export default SearchBar
