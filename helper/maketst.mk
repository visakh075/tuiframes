# tests : tsts_intro bin_dirs $(TST_BIN)
tsts_main : tsts_setup tsts_intro print_tsts tsts_worker
tsts_setup: bin_dirs libs
	@date>>$(LOG_PATH)tests_builds.log
tsts_intro :
	@echo "$(CYAN)TESTS$(RESET)"
	@echo Path: $(TST_BIN_PATH)
tsts_logs:
	@echo "$(YELLOW)$(LOG_PATH)tests_builds.log$(RESET)"
tsts_close:tsts_logs
	@echo "$(GREEN)Done$(RESET)" $(DONE)
tsts_worker_intro:
	@echo Compiling
tsts_worker: tsts_worker_intro $(TST_BIN)
print_tsts:
	@echo Expected Targets
	@ for item in $(TST_BIN); do \
		echo '-' $$item;\
	done
