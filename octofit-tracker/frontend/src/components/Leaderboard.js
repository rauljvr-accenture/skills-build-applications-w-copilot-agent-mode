
const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

function Leaderboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    console.log('Fetching Leaderboard from:', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Leaderboard data:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, []);

  const headers = data && data.length > 0 ? Object.keys(data[0]) : [];

  return (
    <div className="card shadow-sm mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4 text-primary">Leaderboard</h2>
        {data && data.length > 0 ? (
          <div className="table-responsive">
            <table className="table table-striped table-bordered align-middle">
              <thead className="table-light">
                <tr>
                  {headers.map((header) => (
                    <th key={header}>{header.charAt(0).toUpperCase() + header.slice(1)}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {data.map((item, idx) => (
                  <tr key={item.id || idx}>
                    {headers.map((header) => (
                      <td key={header}>{typeof item[header] === 'object' ? JSON.stringify(item[header]) : item[header]}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="alert alert-info">No leaderboard data found.</div>
        )}
      </div>
    </div>
  );
}

export default Leaderboard;
