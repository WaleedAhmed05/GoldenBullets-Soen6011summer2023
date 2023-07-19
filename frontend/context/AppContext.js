import { useState, useEffect, createContext, useContext } from 'react'
import { useRouter } from 'next/router'

const AppContext = createContext()

const AppProvider = ({ children }) => {
	const [user, setUser] = useState(null)
	const [token, setToken] = useState(null)
	const router = useRouter()

	useEffect(() => {
		// Get access token from url param
		const urlParams = new URLSearchParams(window.location.search)
		const accessToken = urlParams.get('token') || urlParams.get('access_token') || localStorage.getItem('_access_token')
		if (accessToken && !user) {
			// Set access token to state
			setToken(accessToken)
			// Get user info from backend with access token
			const isLoggedIn = getUser(accessToken)
			if (isLoggedIn) {
				// Save access token to local storage
				localStorage.setItem('_access_token', accessToken)
				// Redirect to homepage if url contains access token
				if (urlParams.get('token') || urlParams.get('access_token')) {
					router.push('/')
				}
			}
		}
	}, [user])

	const logout = () => {
		// Remove access token from local storage
		localStorage.removeItem('_access_token')
		// Remove user from state
		setUser(null)
	}

	const getUser = async (accessToken) => {
		try {
			const response = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/auth/user`, {
				headers: {
					Authorization: `Bearer ${accessToken}`
				}
			})
			if (response.ok) {
				const user = await response.json()
				setUser(user)
				return true
			}
		} catch (error) {
			console.error('Error fetching user in AppContext', error)
		}
	}

	return (
		<AppContext.Provider value={{ user, token, logout }}>
			{children}
		</AppContext.Provider>
	)
}

const useAppContext = () => useContext(AppContext)

export { AppContext, AppProvider, useAppContext }