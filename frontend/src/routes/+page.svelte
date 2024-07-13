<script>
	let response = null;

	async function fetchData() {
		try {
			const res = await fetch('http://www.localhost:8000/random');
			const data = await res.json();
			response = data;
			console.log(data);
		} catch (error) {
			console.error(error);
		}
	}
</script>

<style>
	.container {
		height: 100vh;
		width: 100vw;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		max-width: 100%;
	}
	.dice {
		display: flex;
		justify-content: center;
		align-items: center;
		width: 150px;
		height: 150px;
		padding: 10px;
		border: 2px solid #000;
		border-radius: 10px;
		margin-bottom: 20px;
		position: relative;
	}
	.grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		grid-template-rows: repeat(3, 1fr);
		width: 100%;
		height: 100%;
	}
	.dot {
		width: 30px;
		height: 30px;
		background-color: #000;
		border-radius: 50%;
		justify-self: center;
		align-self: center;
	}
	button {
		padding: 10px 20px;
		font-size: 16px;
		cursor: pointer;
		border: none;
		border-radius: 5px;
		background-color: #007bff;
		color: #fff;
	}
	button:hover {
		background-color: #0056b3;
	}
	.center-text {
		position: absolute;
		text-align: center;
	}
</style>

<div class="container">
	<div class="dice">
		{#if response === null}
			<p class="center-text">Click to start</p>
		{:else}
			<div class="grid">
				{#if response === 1}
					<div></div><div></div><div></div>
					<div></div><div class="dot"></div><div></div>
					<div></div><div></div><div></div>
				{:else if response === 2}
					<div class="dot"></div><div></div><div></div>
					<div></div><div></div><div></div>
					<div></div><div></div><div class="dot"></div>
				{:else if response === 3}
					<div class="dot"></div><div></div><div></div>
					<div></div><div class="dot"></div><div></div>
					<div></div><div></div><div class="dot"></div>
				{:else if response === 4}
					<div class="dot"></div><div></div><div class="dot"></div>
					<div></div><div></div><div></div>
					<div class="dot"></div><div></div><div class="dot"></div>
				{:else if response === 5}
					<div class="dot"></div><div></div><div class="dot"></div>
					<div></div><div class="dot"></div><div></div>
					<div class="dot"></div><div></div><div class="dot"></div>
				{:else if response === 6}
					<div class="dot"></div><div></div><div class="dot"></div>
					<div class="dot"></div><div></div><div class="dot"></div>
					<div class="dot"></div><div></div><div class="dot"></div>
				{/if}
			</div>
		{/if}
	</div>
	<button on:click={fetchData}>Roll Dice</button>
</div>
