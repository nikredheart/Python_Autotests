run_tests: # Запуск тестов в дефолтном виде
	echo 'before tests'
	call C:\miniconda3\condabin\conda.bat activate python-autotests-basic && \
	python -m pytest && \
	call C:\miniconda3\condabin\conda.bat deactivate && \
	echo 'after tests'



re_run_tests: # Выполнение тестов с перезапуском проваленных
	echo 'before tests'
	call C:\miniconda3\condabin\conda.bat activate python-autotests-basic && \
	python -m pytest --reruns 1 && \
	call C:\miniconda3\condabin\conda.bat deactivate && \
	echo 'after tests'


show_cases: # Отображение в консоли информации о существующих тестах
	echo 'show cases...'
	call C:\miniconda3\condabin\conda.bat activate python-autotests-basic && \
	python -m pytest --collect-only && \
	call C:\miniconda3\condabin\conda.bat deactivate && \
	echo 'show completed'