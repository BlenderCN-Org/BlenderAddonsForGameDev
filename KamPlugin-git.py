import bpy

############# UI ##################################################################################
class InfoPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_idname = "OBJECT_PT_VIEW3D_P1"
    bl_category = 'K&M T00LZ'
    bl_label = "Info"


    def draw(self, context):
        self.layout.label(
            text = "Toto jsou nase pomocne scripty. Copyright Kozlik & Matka Productions",
        )
        
        self.layout.label(
            text = "Pouzivejte s rozvahou",
            icon = 'ERROR',    
        )
        
        self.layout.label(
            text = "Kontakt: kamproductionscz@gmail.com",
        )
                
    def draw_header(self, context):
        self.layout.label(
            text = "",
            icon = 'QUESTION',    
        )

    @classmethod
    def poll(cls, context):
        return (context.object is not None)



class UnrealExportPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_idname = "OBJECT_PT_VIEW3D_P2"
    bl_label = "Unreal Export"
    bl_category = 'K&M T00LZ'


    def draw(self, context):
        self.layout.label("Export projektu do Unrealu")
        self.layout.separator()
        self.layout.operator("object.ue_export_operator")
        
        

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

        
        
class PanelThree(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_idname = "OBJECT_PT_VIEW3D_P3"
    bl_label = "Panel 3"
    bl_category = 'K&M T00LZ'


    def draw(self, context):
        self.layout.label("Also Small Class")

    @classmethod
    def poll(cls, context):
        return (context.object is not None)







############# OPERATORS ######################################################################
class ExportUEOperator(bpy.types.Operator):
    bl_idname = "object.ue_export_operator"
    bl_label = "Export to Unreal"

    # identifier, name, description, icon, number
    #my_enum = bpy.props.EnumProperty(
    #    items = (
    #        ('ONE', "One", "One description"),
    #        ('TWO', "Two", "Two description"),
    #        ('THREE', "Three", "3 description"),
    #    ),
    #    default = 'ONE'
    #)
            
    #my_float = bpy.props.FloatProperty(name="Some Floating Point")
    #my_bool = bpy.props.BoolProperty(name="Toggle Option")
    #my_string = bpy.props.StringProperty(name="String Value")
    
    def execute(self, context):
        #self.report({'INFO'}, self.my_enum)
        self.report({'INFO'}, "Pomoc")
        
        print("Export Unreal operator starting")        
        
        bpy.ops.export_scene.fbx(
            path_mode               =   'ABSOLUTE',
            filepath                =   "c:\\Users\\mtkew_6rfb1xb\\Desktop\\xaxa\\test.fbx",
            check_existing          =   False,
            axis_forward            =   '-Z',
            axis_up                 =   'Y',
            filter_glob             =   "*.fbx",
            version                 =   'BIN7400',
            # tohle asi nechci ui tab ...
            ui_tab                  =   'MAIN',
            use_selection           =   False,
            global_scale            =   1.0,
            apply_unit_scale        =   True,
            bake_space_transform    =   False,
            object_types            =   {'MESH', 'ARMATURE'},
            use_mesh_modifiers      =   True,
            mesh_smooth_type        =   'FACE',
            # WTF ???
            use_mesh_edges          =   True,
            # WTF ???
            use_tspace              =   False,
            use_custom_props        =   True,
            # Pokud je to true, delaj kosti bordel v Unrealu
            add_leaf_bones          =   False,
            primary_bone_axis       =   'X',
            secondary_bone_axis     =   'Y',
            # Pouzij jenom kosti co deformujou mesh - nebudou se brat v uvahu pomocne kosti, aso True
            # aby se usetrilo misto v animackach
            use_armature_deform_only=   True,
            # Export baked keyframe animations
            bake_anim               =   True,
            # Forcnout exportovani aspon jednoho keye animacek pro kazdou kost
            # Prej potreba pro UE
            bake_anim_use_all_bones =   True,
            # Vyexporti nemutle NLA stripy jako animace, misto jedne globalni animace
            # Asi se hodi pro Unreal pokud nedelame Intro atp...
            # Proste kazdej NLA strip jako anim, cili vice anim v jednom souboru
            bake_anim_use_nla_strips=   True,
            # Vzdycky prida keyframe na zacatek a konec animace - je potreba????
            bake_anim_force_startend_keying = True,
            bake_anim_step          =   1.00,
            bake_anim_simplify_factor = 0,
            # Export keyframe animation ????
            use_anim                =   True,
            # Export all actions or just selected one
            use_anim_action_all     =   True,
            # WTF ?????
            use_default_take        =   True,
            # Remove double keyframes
            use_anim_optimize       =   True,
            anim_optimize_precision =   20,
            embed_textures          =   True,
            # Active scene to file / Each scene as file / Each group as file
            batch_mode              =   'OFF',
            use_batch_own_dir       =   True,
            use_metadata            =   True,
        )
        
        print("Export Unreal operator starting")
        
        return {'FINISHED'}

    #zobrazi okno pro vyplneni hodnot zkusime to bez toho
    #def invoke(self, context, event):
    #    wm = context.window_manager
    #    return wm.invoke_props_dialog(self)
    
    




############# INIT ###########################################################################
bpy.utils.register_class(ExportUEOperator)

bpy.utils.register_class(InfoPanel)
bpy.utils.register_class(UnrealExportPanel)
bpy.utils.register_class(PanelThree)

# Spusteni ze script editoru
if __name__ == "__main__":
    register()