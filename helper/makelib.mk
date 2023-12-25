# LIBRARIES
# Additional Imports
# ..List...
# Own Libs
# ..List...
# Compilation
# ..Worker...
.PHONY : libs_main ModuleSetup ModulesIntro SubModules SubModulesIntro SubModulesBuilds PrjModules PrjModulesWorker libs_logs libs_close


libs_main : ModuleSetup ModulesIntro SubModules PrjModules libs_close

ModuleSetup: bin_dirs
	@date>>"$(LOG_PATH)libs_builds.log"

### SubModules
SUB_MODULES_LIST:=$(shell python3 helper/lib_scan.py SubModules)

SubModules:SubModulesIntro SubModulesWorker
SubModulesIntro:
	@echo ⤵ Sub Modules

SubModulesWorker : $(SUB_MODULES_LIST)
$(SUB_MODULES_LIST):
	@BuildPath=$$(python3 helper/lib_scan.py getBuildPathM $@);\
	ModuleName=$$(python3 helper/lib_scan.py getPrjNameModule $@);\
	echo "$(BLUE)- $@ ∈ $$ModuleName $(RESET)";\
	$(MAKE) -s --directory=$$BuildPath ModuleSetup || exit 1 ;\
	$(MAKE) -s --directory=$$BuildPath obj/$@.o || exit 1 ;\
	echo "$(RESET)$(GREEN)📦$@ ✔ $(RESET)"	

### PrjModules
PRJ_MODULES_LIST:=$(shell python3 helper/lib_scan.py PrjModules)
PrjModules : PrjModulesIntro PrjModulesWorker
PrjModulesIntro :
	@echo "⤵ Prj Modules (Owned)"
PrjModulesWorker : $(PRJ_MODULES_LIST)

$(PRJ_MODULES_LIST):
	@ModuleName=$$(python3 helper/lib_scan.py getPrjNameModule $@);\
	echo "$(BLUE)- $@ $(ModuleName) $(RESET)"

	@$(MAKE) -s obj/$@.o || exit 1
	@echo "$(RESET)$(GREEN)📦$@ ✔ $(RESET)$(GREY)"

ModulesIntro:
	@echo "$(UNDERLINE)$(CYAN)$(BOLD)LIBRARIES - $(PRJ_NAME) $(RESET)"

libs_logs:
	@echo "$(YELLOW)$(LOG_PATH)libs_builds.log$(RESET)"
libs_close:libs_logs
	@echo "$(GREEN)Done$(RESET)" $(DONE)

clean_project: clean
	@echo "$(CYAN)$(BOLD)"CLEAN SUB PROJECTS"$(RESET)"
	

	@$(foreach Module,$(SUB_MODULES_LIST),\
	ModulePath=$(shell python3 helper/lib_scan.py getBuildPathM $(Module));\
	echo "  ""$(BLUE)"$(Module)"$(RESET)";\
	$(MAKE) -s --directory=$$ModulePath clean;\
	echo "  "🗑 $(Module) "$(GREEN)"✔"$(RESET)";\
	)

AR:=ar
packages : libs
	@mkdir -p packages
	@echo "$(CYAN)$(BOLD)"PACKAGES"$(RESET)"
	@$(foreach src,$(PRJ_MODULES_LIST),\
	echo - $(src);\
	ObjectPath=$(shell python3 helper/lib_scan.py getObjectPath $(src));\
	$(AR) rcs packages/$(src).a $$ObjectPath;\
	echo "  "📦$(src).a "$(GREEN)"✔"$(RESET)";\
	HeaderPath=$(shell python3 helper/lib_scan.py getHeaderPath $(src));\
	cp $$HeaderPath packages/;\
	echo "  "$(src).h "$(GREEN)"✔"$(RESET)";\
	)

	@$(foreach src,$(SUB_MODULES_LIST),\
	echo - "$(BLUE)"$(src)"$(RESET)";\
	ObjectPath=$(shell python3 helper/lib_scan.py getObjectPath $(src));\
	$(AR) rcs packages/$(src).a $$ObjectPath;\
	echo "  "📦$(src).a "$(GREEN)"✔"$(RESET)";\
	HeaderPath=$(shell python3 helper/lib_scan.py getHeaderPath $(src));\
	cp $$HeaderPath packages/;\
	echo "  "$(src).h "$(GREEN)"✔"$(RESET)";\
	)
#	$(AR) rcs $(BUILD_DIR)/lib$(LIB_NAME).a $(LIB_OBJ)