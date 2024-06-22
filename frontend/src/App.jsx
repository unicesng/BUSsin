import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import Home from './pages/Home';
import Results from './pages/Results';
import Navbar from './components/navbar';
import { ChakraProvider } from '@chakra-ui/react'

function App() {

  return (
    <ChakraProvider>
      <Router>
        <div className='w-screen h-full'>
          <Navbar/>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/results" element={<Results />} />
          </Routes>
        </div>
      </Router>
    </ChakraProvider>
  )
}

export default App
