run-db:
	docker run --name vwm -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=vwm_db -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
