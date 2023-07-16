export default async (req, res) => {
	try {
		// Get access token from authorization header
		const authHeader = req.headers.authorization
		if (!authHeader) {
			return res.status(401).json({ message: 'Authorization header missing' })
		}
		const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/auth/user`, {
			headers: {
				Authorization: authHeader
			}
		})
		const data = await response.json()
		if (response.ok) {
			return res.status(200).json(data)
		}
		return res.status(401).json({ message: data.message })
	} catch (error) {
		console.error('Error fetching user in api/auth/user', error)
		return res.status(403).json({ message: 'User forbidden' })
	}
}