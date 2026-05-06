function ResultDisplay({ result }){
    if (!result) return null;

    return (
        <div style={{ marginTop: "2rem" }}>
            <h2>Result:</h2>
            <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
    );
}

export default ResultDisplay;