export default async (req, res) => {
	try {
		// Get access token from authorization header
		const authHeader = req.headers.authorization
		if (!authHeader) {
			return res.status(401).json({ message: 'Authorization header missing' })
		}
		if (req.method === 'GET') {
			if (req.query.filter === '') {
				const response = await fetch(`${process.env.API_URL}/api/jobs/search/filter?job_type=${req.query.job_type}`, {
					method: 'GET',
					headers: {
						Authorization: authHeader,
						'Content-Type': 'application/json',
					},
				})
				const data = await response.json()
				if (response.ok) {
					return res.status(200).json(data)
				}
			} else {
				// Url encode the query string
				const query = encodeURIComponent(req.query.q)
				// Send a GET request to the API to search jobs
				const response = await fetch(`${process.env.API_URL}/api/jobs/search?q=${query}`, {
					method: 'GET',
					headers: {
						Authorization: authHeader,
						'Content-Type': 'application/json',
					},
				})
				const data = await response.json()
				if (response.ok) {
					return res.status(200).json(data)
				}
			}
		} else {
			return res.status(405).json({ message: 'Method not allowed' })
		}
	} catch (error) {
		console.error('Error accessing api/jobs/search', error)
		return res.status(403).json({ message: 'User forbidden' })
	}
}