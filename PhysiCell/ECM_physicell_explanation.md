

# cell_ECM_interactions
___

# void copy_ECM_data_to_BioFVM( void);
- Permet d'utiliser les règles sur les comportement des cellules ainsi que dans studio
(Déconseillé d'utiliser les règles pour modifier des aspects mechaniques comme la vitesse parce que actualisé trop rarement)
- Récupère l'anisotropie et la densité
- L'associe au vecteur densité de BIOFVM


# double dot_product_ext( const std::vector<double>& v , const std::vector<double>& w );
- fonction pour un produit scalaire

# double sign_function (double number);
- si négatif retourne -1
- si positif retourne 1

# void custom_update_cell_velocity( Cell* pCell, Phenotype& phenotype, double dt);
- version customisé de update_motility_vector
- aléatoirement au cours du temps
    - récupère link_anisotropy_and_bias et ECM_sensitivité
    - Choisis une direction random
    - si fonction de update migration l'execute
    - selon la valeur de link_anisotropy_and_bias
        - màj de migration_bias_direction

# void ECM_to_cell_interactions(Cell* pCell, Phenotype& phenotype, double dt);
- fonction qui calcules la direction selon la chimiotaxie et les fibres
- calcule ensuite la vitesse selon ECM density

# void ECM_remodeling_function( Cell* pCell, Phenotype& phenotype, double dt );
- fonction qui màj la matrice
- modifie la densité selon les cellules présentes
- Réalignement des fibre en fonction de la direction de migration
- Modidifie l'anisotropie du voxel 

# void custom_update_motility_vector( Cell* pCell, Phenotype& phenotype, double dt_  );
- remplace standard_update_cell_velocity
- fais appels aux fonctions : 
    - custom_update_motility vector
    - EMC_to_cell_interactions


# void create_default_ECM_compatible_agent( void );
- attribue les nouvelles fonctions custome aux différentes cellules (custome_update_cell_velocity et ECM_remodelling)

# void SVG_plot_custom( std::string filename , Microenvironment& M, double z_slice , double time, std::vector<std::string> (*cell_coloring_function)(Cell*), std::string line_pattern );

# void write_ECM_Data_matlab( std::string filename );

## extracellular_matrix
___

# class ECM_Cartesian_Mesh : public Cartesian_Mesh
- ECM_Cartesian_Mesh();


# class ECM_Voxel : public Voxel
- ECM_Voxel();

	double anisotropy;
	double density;
	std::vector<double> ecm_fiber_alignment;

# class ECM
- ECM_Voxel ecm_voxel;
	ECM_Cartesian_Mesh ecm_mesh;
	std::string spatial_units; 
	std::string name; 
	std::vector<ECM_Voxel> ecm_voxels;



	ECM();
	ECM(std::string name);

    # void make_ecm_units (void);

	# void resize_ecm_units_from_ecm_mesh(void); // destroys previous ECM vector. New ECM_units are put in place and any previous initial configuration is lost

	# void initialize_ECM(void);



# class ECM_options
- ECM* pECM;
	std::string name; 

	std::string spatial_units; 
	double dx;
	double dy; 
	double dz; 

	// Currently only used to specify FIBER orientation, but could be expanded in the future
	std::string ecm_initial_configuration;

	ECM_options(); // needs defined!!!


___

# invasion_uncoupled

___



# void chemotaxis_oxygen( Cell* pCell , Phenotype& phenotype , double dt ); 
- pas utilisé

# void rightward_deterministic_cell_march (Cell* pCell , Phenotype& phenotype , double dt );
- pas utilisé si march_unit_test_setup = 0 (oui)

# void reset_cell_position(void);
- utiliser dans main, comprends pas a quoi ça sert

# void create_cell_types( void ); 
- créer les agents compatible ECM
- mise en place des différentes définitions (cells, behavior, rules)
- màj le définition de cell en particulier (leader,follower)
    - leader_cell -> custom_update_cell_velocity + custom cell_rule
    - follower_cell -> custom_update_cell_velocity

# void setup_extracellular_matrix( void ); 
- important


# void setup_tissue(void); // done 
- je l'ai bidouillé pour que ça soit le csv que je veux mais normalement changer les params initiaux (lesion = csv)

# void setup_microenvironment( void );  // done 
- initialize microenv () vide

# std::vector<std::string> AMIGOS_invasion_coloring_function( Cell* );
- utilisé


- Les 3 prochains dépendent de cell_motility_ECM_interaction_model_selector


# void ECM_informed_motility_update_w_chemotaxis ( Cell* pCell, Phenotype& phenotype, double dt );

- bizarre on dirait que ça fait tous les trucs de la lib sans utiliser les mêmes méthodes
- si cell dead -> devient immobile
- màj de la direction de migration
    - même chose que custom_update_motility
- màj de la vitesse
# void ECM_informed_motility_update_model_w_memory ( Cell* pCell, Phenotype& phenotype, double dt ); // Uses previous migration bias direction


# void ECM_informed_motility_update_w_chemotaxis_w_variable_speed( Cell* pCell, Phenotype& phenotype, double dt ); // Sets speed based on fiber alignment. If chemo senstivitty set to 1, then cells will chemotax with speed varying strictly with alignemnt.


# void ecm_update_from_cell_motility_vector(Cell* pCell , Phenotype& phenotype , double dt);
- utilisé

void ecm_update_from_cell_velocity_vector(Cell* pCell , Phenotype& phenotype , double dt);
# void run_biotransport( double t_max );
- permet d'init sans erreurs
# void alter_cell_uptake_secretion_saturation ( void );
- si le param freeze_uE_profile == false ne fait rien (normalement oui)

void set_cell_motility_vectors(void); // Runs update_migration_bias for each cell present in a simulation
// void SVG_plot_custom( std::string filename , Microenvironment& M, double z_slice , double time, std::vector<std::string> (*cell_coloring_function)(Cell*), std::string line_pattern );
